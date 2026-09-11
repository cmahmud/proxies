# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 425
- HTTP: 94 alive / 67 gold
- HTTPS: 55 alive / 21 gold
- SOCKS4: 187 alive / 166 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48898
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
