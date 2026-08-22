# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 417
- HTTP: 268 alive / 84 gold
- HTTPS: 207 alive / 22 gold
- SOCKS4: 216 alive / 141 gold
- SOCKS5: 283 alive / 170 gold

## Historical pool

- Discovered: 164957
- Ever alive: 32224
- Ever gold: 1175

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
