# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 423
- HTTP: 99 alive / 66 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 194 alive / 165 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48912
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
