# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 423
- HTTP: 97 alive / 64 gold
- HTTPS: 49 alive / 21 gold
- SOCKS4: 198 alive / 166 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48911
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
