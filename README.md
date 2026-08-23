# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 216
- HTTP: 135 alive / 35 gold
- HTTPS: 77 alive / 6 gold
- SOCKS4: 170 alive / 86 gold
- SOCKS5: 183 alive / 89 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
