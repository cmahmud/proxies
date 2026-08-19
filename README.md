# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 540
- HTTP: 413 alive / 155 gold
- HTTPS: 274 alive / 105 gold
- SOCKS4: 214 alive / 137 gold
- SOCKS5: 211 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19839
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
