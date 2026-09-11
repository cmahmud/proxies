# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 419
- HTTP: 84 alive / 65 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 189 alive / 164 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48885
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
