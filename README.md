# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 531
- HTTP: 379 alive / 159 gold
- HTTPS: 273 alive / 88 gold
- SOCKS4: 233 alive / 153 gold
- SOCKS5: 203 alive / 131 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18163
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
