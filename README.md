# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 418
- HTTP: 335 alive / 94 gold
- HTTPS: 243 alive / 24 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 258 alive / 159 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30115
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
