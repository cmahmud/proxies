# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 423
- HTTP: 323 alive / 83 gold
- HTTPS: 202 alive / 32 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 250 alive / 164 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31511
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
