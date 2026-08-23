# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 210
- HTTP: 131 alive / 35 gold
- HTTPS: 147 alive / 7 gold
- SOCKS4: 185 alive / 77 gold
- SOCKS5: 207 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
