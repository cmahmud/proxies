# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 410
- HTTP: 91 alive / 62 gold
- HTTPS: 39 alive / 22 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48822
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
