# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 461
- HTTP: 126 alive / 93 gold
- HTTPS: 50 alive / 29 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49426
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
