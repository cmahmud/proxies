# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 425
- HTTP: 89 alive / 66 gold
- HTTPS: 49 alive / 23 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48893
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
