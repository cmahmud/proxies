# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 427
- HTTP: 99 alive / 66 gold
- HTTPS: 49 alive / 19 gold
- SOCKS4: 193 alive / 166 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48907
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
