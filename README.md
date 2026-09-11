# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 419
- HTTP: 105 alive / 65 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 193 alive / 163 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48917
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
