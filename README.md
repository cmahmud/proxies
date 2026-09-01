# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 452
- HTTP: 118 alive / 88 gold
- HTTPS: 130 alive / 29 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 221 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46572
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
