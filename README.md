# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 466
- HTTP: 120 alive / 94 gold
- HTTPS: 49 alive / 30 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49419
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
