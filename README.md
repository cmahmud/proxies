# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 459
- HTTP: 145 alive / 89 gold
- HTTPS: 143 alive / 32 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 183 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46654
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
