# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 466
- HTTP: 121 alive / 94 gold
- HTTPS: 49 alive / 30 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49419
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
