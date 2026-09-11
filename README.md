# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 421
- HTTP: 103 alive / 66 gold
- HTTPS: 49 alive / 20 gold
- SOCKS4: 190 alive / 164 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48917
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
