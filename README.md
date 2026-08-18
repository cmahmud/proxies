# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 226
- HTTP: 272 alive / 30 gold
- HTTPS: 106 alive / 8 gold
- SOCKS4: 204 alive / 116 gold
- SOCKS5: 205 alive / 72 gold

## Historical pool

- Discovered: 92563
- Ever alive: 9315
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
