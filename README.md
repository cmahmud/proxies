# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 554
- HTTP: 418 alive / 191 gold
- HTTPS: 300 alive / 83 gold
- SOCKS4: 224 alive / 134 gold
- SOCKS5: 205 alive / 146 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19826
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
