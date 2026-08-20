# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 358
- HTTP: 154 alive / 57 gold
- HTTPS: 117 alive / 18 gold
- SOCKS4: 196 alive / 142 gold
- SOCKS5: 221 alive / 141 gold

## Historical pool

- Discovered: 147647
- Ever alive: 25865
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
