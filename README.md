# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 426
- HTTP: 99 alive / 64 gold
- HTTPS: 52 alive / 20 gold
- SOCKS4: 194 alive / 166 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48908
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
