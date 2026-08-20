# SyndProxy private pool

## Current pool

- Alive now: 1758
- Gold now: 650
- HTTP: 702 alive / 217 gold
- HTTPS: 501 alive / 121 gold
- SOCKS4: 223 alive / 151 gold
- SOCKS5: 332 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24194
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
