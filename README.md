# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 352
- HTTP: 196 alive / 65 gold
- HTTPS: 141 alive / 18 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 210 alive / 125 gold

## Historical pool

- Discovered: 145547
- Ever alive: 25392
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
