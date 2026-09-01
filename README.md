# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 464
- HTTP: 131 alive / 94 gold
- HTTPS: 132 alive / 31 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46670
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
