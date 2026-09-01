# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 464
- HTTP: 130 alive / 94 gold
- HTTPS: 125 alive / 31 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46672
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
