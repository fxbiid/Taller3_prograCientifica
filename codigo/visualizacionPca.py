from sklearn.decomposition import PCA


class VisualizacionPca:

    def reducir_dimensiones(self, matriz, componentes=2):

        pca = PCA(n_components=componentes)

        resultado = pca.fit_transform(matriz)

        return resultado, pca.explained_variance_ratio_