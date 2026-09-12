# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 469
- HTTP: 129 alive / 94 gold
- HTTPS: 65 alive / 36 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49393
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
