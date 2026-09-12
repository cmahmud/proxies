# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 417
- HTTP: 106 alive / 76 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49459
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
