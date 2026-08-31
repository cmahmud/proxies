# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 455
- HTTP: 158 alive / 88 gold
- HTTPS: 132 alive / 31 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 232 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45315
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
