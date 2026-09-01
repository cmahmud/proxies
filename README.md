# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 457
- HTTP: 139 alive / 89 gold
- HTTPS: 143 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46636
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
