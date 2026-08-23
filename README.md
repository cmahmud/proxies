# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 200
- HTTP: 130 alive / 34 gold
- HTTPS: 144 alive / 7 gold
- SOCKS4: 199 alive / 68 gold
- SOCKS5: 208 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
