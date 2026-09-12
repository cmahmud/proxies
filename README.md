# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 466
- HTTP: 125 alive / 93 gold
- HTTPS: 52 alive / 37 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49402
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
