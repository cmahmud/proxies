# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 462
- HTTP: 129 alive / 94 gold
- HTTPS: 56 alive / 28 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49424
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
