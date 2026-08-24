# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 380
- HTTP: 123 alive / 49 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33535
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
