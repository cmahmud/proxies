# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 402
- HTTP: 182 alive / 93 gold
- HTTPS: 134 alive / 21 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 221 alive / 150 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29176
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
