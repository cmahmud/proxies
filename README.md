# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 210
- HTTP: 132 alive / 35 gold
- HTTPS: 152 alive / 7 gold
- SOCKS4: 184 alive / 77 gold
- SOCKS5: 205 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
