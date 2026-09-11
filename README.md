# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 424
- HTTP: 89 alive / 67 gold
- HTTPS: 51 alive / 22 gold
- SOCKS4: 186 alive / 166 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48897
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
