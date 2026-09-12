# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 460
- HTTP: 128 alive / 93 gold
- HTTPS: 58 alive / 31 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49406
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
