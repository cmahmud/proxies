# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 479
- HTTP: 330 alive / 144 gold
- HTTPS: 254 alive / 87 gold
- SOCKS4: 203 alive / 118 gold
- SOCKS5: 225 alive / 130 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17572
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
