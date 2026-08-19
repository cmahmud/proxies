# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 552
- HTTP: 440 alive / 191 gold
- HTTPS: 306 alive / 84 gold
- SOCKS4: 223 alive / 131 gold
- SOCKS5: 207 alive / 146 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19826
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
