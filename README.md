# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 402
- HTTP: 184 alive / 80 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 228 alive / 155 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 150516
- Ever alive: 27035
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
