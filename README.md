# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 427
- HTTP: 94 alive / 65 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 195 alive / 166 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48908
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
