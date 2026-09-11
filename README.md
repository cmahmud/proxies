# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 426
- HTTP: 95 alive / 66 gold
- HTTPS: 53 alive / 21 gold
- SOCKS4: 185 alive / 166 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48898
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
