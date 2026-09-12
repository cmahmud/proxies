# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 440
- HTTP: 113 alive / 86 gold
- HTTPS: 56 alive / 32 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49440
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
