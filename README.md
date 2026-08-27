# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 404
- HTTP: 98 alive / 62 gold
- HTTPS: 170 alive / 15 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41035
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
