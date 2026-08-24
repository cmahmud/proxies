# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 390
- HTTP: 123 alive / 66 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33281
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
