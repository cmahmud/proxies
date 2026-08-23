# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 343
- HTTP: 113 alive / 40 gold
- HTTPS: 72 alive / 11 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 181 alive / 140 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32815
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
