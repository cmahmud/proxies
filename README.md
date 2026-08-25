# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 416
- HTTP: 93 alive / 59 gold
- HTTPS: 72 alive / 21 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36208
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
