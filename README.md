# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 461
- HTTP: 140 alive / 92 gold
- HTTPS: 130 alive / 31 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46664
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
